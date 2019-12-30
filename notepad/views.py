from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Note
from .forms import NoteModelForm
# Create your views here.

#CRUD

def create_note(request):
    form =NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user=request.user
        print("before saving the form")
        form.save()
        print("after saving the form")
        return redirect('/notes/list/')
    context={
        'form':form
    }
    return render(request,"notepad/create.html",context)
    

def list_notes(request):
    all_notes=Note.objects.all()
    context ={
        "all_notes":all_notes
    }
    return render(request,"notepad/list.html",context)


def delete_note(request,id):
    
    selected_note = get_object_or_404(Note,pk=id)
    if selected_note:
        if selected_note.user == request.user:
            selected_note.delete()
            message.info("Successfully deleted the note")
        else:
            message.info("You don't have rights to delete the note")
    else:
        message.info("The specified note with id {} doesnot exist".format(id))
    return redirect('/notes/list/')

def update_note(request,id):
    selected_note = get_object_or_404(Note,pk=id)
    form =NoteModelForm(request.POST or None, request.FILES or None,instance=selected_note)
    if form.is_valid():
        form.instance.user=request.user
        print("before saving the form")
        form.save()
        print("after saving the form")
        return redirect('/notes/list')
    context={
        'form':form
    }
    return render(request,"notepad/create.html",context)
    
