from django.shortcuts import render

from .models import Topic


def index(request):
    """strona główna dl aplikacji"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """wyświetlanie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """wyświetla pojedynczy temat i wszystki powiązane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

