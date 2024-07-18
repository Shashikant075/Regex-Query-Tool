from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import RegexQueryForm
from .models import TextEntry
import re



def regex_query(request):
    form = RegexQueryForm()
    matches = None
    db_matches = None

    if request.method == 'POST':
        form = RegexQueryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            pattern = form.cleaned_data['pattern']
            search_in_db = form.cleaned_data['search_in_db']
            
            try:
                if text:
                    matches = re.findall(pattern, text)
                if search_in_db:
                    db_matches = []
                    for entry in TextEntry.objects.all():
                        entry_matches = re.findall(pattern, entry.text)
                        if entry_matches:
                            db_matches.append((entry, entry_matches))
            except re.error as e:
                form.add_error('pattern', f"Invalid regex pattern: {e}")

    return render(request, 'regex_query/regex_query.html', {'form': form, 'matches': matches, 'db_matches': db_matches})
