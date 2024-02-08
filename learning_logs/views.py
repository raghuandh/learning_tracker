from django.shortcuts import render
from . models import Topic, Entry, DiaryEntry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm, DiaryEntryForm
# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # restricting users to only login
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)
@login_required
def Diary(request):
    entries = DiaryEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'learning_logs/Diary.html', context)
@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    context = {'entry':entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
@login_required
def new_diary_entry(request):
    #entry = Entry.objects.get()
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Diary'))
    else:
        form = DiaryEntryForm()
    return render(request, 'learning_logs/new_diary_entry.html', {'form': form})
@login_required
def diary_entry_edit(request, entry_id):
    entry = DiaryEntry.objects.get(id=entry_id)
    if request.method != 'POST':
        form = DiaryEntryForm(instance=entry)

    else:
        form = DiaryEntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Diary'))
    context = {'entry':entry,'form': form,}
    return render(request, 'learning_logs/diary_entry_edit.html', context)