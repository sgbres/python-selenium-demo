# 🎮 Twitch Mobile UI Automation with Selenium & Pytest

This project is a robust and scalable mobile browser automation test using **Selenium (Python)**. It automates a Twitch search and streamer navigation using **Google Chrome’s mobile emulator**.

## ✅ Test Case Steps

1. Open Twitch.tv on a mobile emulator.
2. Click the search icon.
3. Enter `StarCraft II`.
4. Scroll down twice to load more streams.
5. Select a streamer from the results.
6. Handle any modal/pop-ups.
7. Wait for stream content to fully load.
8. Capture a screenshot.

## 📹 Demo

![Test Running Demo](demo/twitch_mobile_demo.gif)

## 🧱 Project Structure

| Folder/File       | Purpose |
|-------------------|---------|
| `tests/`          | Test cases using `pytest` |
| `pages/`          | Page Object Models (POM) for UI elements |
| `utils/`          | Helpers for driver setup, screenshots, and pop-up handling |
| `screenshots/`    | Output folder for screenshots |
| `conftest.py`     | Pytest fixture for browser setup |
| `requirements.txt`| Dependencies |
| `pytest.ini`      | Pytest config |

## 🚀 Running the Test

### 1. Install dependencies

```bash
pipenv install
```
### 2. Run the test
```
pytest tests/test_twitch_search.py
```

## 💡 Notes

- Uses Pixel 5 emulation for mobile responsiveness.
- Handles Twitch modals/popups.
- Screenshot is saved in /screenshots with a timestamp.

## 🧪 Tools Used

- Selenium 4+
- Pytest