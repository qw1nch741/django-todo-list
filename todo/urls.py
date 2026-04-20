from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from todo.views import TaskListView, Index, TaskCreateView, TaskUpdateView, TaskUndoView, TagListView, TagUpdateView, \
    TagCreateView, TaskDeleteView, TagDeleteView

app_name = "todo"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    #task views
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/undo/', TaskUndoView.as_view(), name='task-undo'),
    #tag views
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
