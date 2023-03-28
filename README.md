# Flask App Template with Loading Page

This template provides a basic structure for a Flask app with a loading page while processing data.

## How It Works

1. The `index.html` page contains a button with the ID `start-process`. This ID is used to associate the button with a JavaScript event listener.
2. In the JavaScript code within `index.html`, the `document.getElementById("start-process")` function is used to select the button by its ID.
3. An event listener is attached to the button, and when the button is clicked, the listener triggers a function that redirects the user to the `loading.html` page using the `window.location.href` JavaScript property.
4. The `loading.html` page displays a loading spinner while the data processing is being done in the background.
5. Once the data processing is complete, the script on the `loading.html` page redirects the user back to the `index.html` page.

## Usage

1. Clone or download this repository.
2. Install Flask if you haven't already: `pip install Flask`
3. Navigate to the project directory.
4. Run `app.py`: `python app.py`
5. Open a browser and go to `http://127.0.0.1:5000/` to see the app in action.

## Customization

- Update the `app.py` file to include your specific data processing functions and routes.
- Modify the `templates/index.html` and `templates/loading.html` files to include your desired content and styles.
  - For example, you may want to change the content displayed on the main page, modify the loading spinner, or update the button's functionality.
  - To customize the button, simply update the event listener function in `templates/index.html` with your desired actions.
- Add any additional templates to the `templates/` folder as needed.
- Customize the styles in `static/css/styles.css`.

## License

This project is licensed under the MIT License.
