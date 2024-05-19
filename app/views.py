from django.shortcuts import render
from .models import Candidate
from django.shortcuts import render, get_object_or_404
def index(request):
    # Assuming you want to show the resume of a specific candidate.
    # Replace `1` with the ID of the candidate you want to display
    candidate = get_object_or_404(Candidate, id=1)
    return render(request, 'index.html', {'candidate': candidate})