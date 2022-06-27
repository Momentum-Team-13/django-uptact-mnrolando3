Task 1:
- familiarize yourself with Django

- If I wanted to add a new URL to this project, what two files would I edit? Views and URLs

- If I wanted to add a birthday to each contact, what file would I edit? Database to add information; list_contacts.html to add field

    - Add a birthday field to the `Contact` model. This field should be of type `DateField` and should be allowed to be null and empty.
    - Make sure you can edit the birthday by changing the `ContactForm`.
    - Add the ability to display the birthday on the list of contacts. You will have to edit `templates/contacts/list_contacts.html`.

When you get through that, add a birthday to one of your contacts to test out your code.
