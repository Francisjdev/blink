# Blink Aid

## Inspiration

This project was born from a personal need: my father has a condition
that limits his ability to speak and move. I wanted to build a simple,
accessible way for him to request help using only his eyes.
Blink Aid detects rapid blinks and automatically sends a WhatsApp
message through Twilio --- turning a small gesture into a clear signal
for assistance.

------------------------------------------------------------------------

## Features

-   **Blink Detection:** Uses
    [MediaPipe](https://developers.google.com/mediapipe) and
    [OpenCV](https://opencv.org/) to identify real-time eye blinks
    through a webcam.
-   **Smart Trigger Logic:** Counts the number of blinks within a short
    time window to avoid false positives.
-   **WhatsApp Notification:** Integrates with
    [Twilio](https://www.twilio.com/) to send instant WhatsApp alerts
    when a trigger condition is met.

------------------------------------------------------------------------

## Tech Stack

-   **Language:** Python
-   **Libraries:** MediaPipe, OpenCV, Twilio

------------------------------------------------------------------------

## Setup and Usage

### 1. Clone this repository

``` bash
git clone https://github.com/Francisjdev/blink.git
cd blink
```

### 2. Create a virtual environment

``` bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Set up environment variables

This project uses **Twilio's WhatsApp Sandbox** for testing purposes.
To enable message notifications, you will need a **Twilio account** and
access to the **WhatsApp Sandbox**.

#### Setup steps:

1.  Create an account on [Twilio](https://www.twilio.com/).\
2.  Navigate to **Messaging → Try it out → Send a WhatsApp message**.
3.  Follow Twilio's instructions to connect your phone number to the
    sandbox.
4.  Create a `.env` file in the project root with the following
    variables:

``` bash
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+your_phone_number
```

⚠️ Important: This project uses Twilio's sandbox for development and
testing.\
Messages are limited to sandbox-approved numbers and are not suitable
for production use.

------------------------------------------------------------------------

### 5. Run the app

``` bash
python main.py
```

------------------------------------------------------------------------

## Example Behavior

-   When three blinks occur within one second, a WhatsApp message is
    sent (e.g., "I need something").
-   This logic can be easily customized for other gestures or message
    types.

------------------------------------------------------------------------

## Future Improvements

-   Add configurable sensitivity and message templates
-   Support for multiple contacts
-   Lightweight UI for setup and monitoring
-   Potential integration with IoT devices (lights, alarms, etc.)

------------------------------------------------------------------------


## A Note

This project started as a way to help my dad --- but it became more than
that.\
It's a reminder that technology can be deeply human when built with
empathy.
