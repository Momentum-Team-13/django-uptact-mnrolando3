from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})
# defines function for list_contacts with all contact objects
# will load the list of contacts


def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/view_contact.html', {'contact': contact})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
        # if add_contact is requested, the form should be the ContactForm
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')
            # else post the data; if form is valid save and return to list

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})


def add_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to='view_contact')

    return render(request, "contacts/add_note.html", {"form": form},
                  {"note": note})
# add_note copying edit_contact format

# def add_note(request):
#     if request.method == 'GET':
#         form = NoteForm()
#     else:
#         form = NoteForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='view_contact')

#     return render(request, "contacts/add_note.html", {"form": form})
# # add_note copying add_contact format
