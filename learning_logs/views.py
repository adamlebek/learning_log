from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


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

def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != 'POST':
        #nie przekazano żadnych danych, należy utwożyć pusty formularz
        form = TopicForm()
    else:
        #przekazano dane za pomocą żądania POST, należy je przetworzyć
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    #wyświetlanie pustego formularza
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)