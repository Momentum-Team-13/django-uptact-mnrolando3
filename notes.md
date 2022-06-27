Task 1:
- Familiarize yourself with Django

- If I wanted to add a new URL to this project, what two files would I edit? Views and URLs

- If I wanted to add a birthday to each contact, what file would I edit? Database to add information; list_contacts.html to add field

    - Add a birthday field to the `Contact` model. This field should be of type `DateField` and should be allowed to be null and empty.
    - Make sure you can edit the birthday by changing the `ContactForm`.
    - Add the ability to display the birthday on the list of contacts. You will have to edit `templates/contacts/list_contacts.html`.

When you get through that, add a birthday to one of your contacts to test out your code.


Task 2:
- Explore relationships between models, and how URLs and views work

- If I wanted to add a new model, where would I do that? models.py

- If I wanted to connect the new model to the `Contact` model, how would I do that? add it to contacts>models.py then migrate

- Add a new model, `Note`, to the `contacts` app.
    - This model should contain text for the note and the date/time of the note. Look at the `auto_now_add` option for the `DateTimeField` to have the date/time automatically populated.
- Connect the `Note` model to the `Contact` model using a `ForeignKey`.
- Use the Django console to add a note to one of your contacts.
- Make a new view and template to see an individual contact. The URL for this view should be `contacts/<int:pk>/`. Show the notes for that contact on this individual view. Otherwise, this page can look like an individual contact on the contacts list page.