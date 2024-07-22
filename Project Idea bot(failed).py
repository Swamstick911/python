from slack_bolt import App
from pyngrok import ngrok, conf
import os

# Add bin directory to PATH (optional, but might be needed)
os.environ["PATH"] += os.pathsep + os.path.expanduser("~/bin")

# Set ngrok configuration to use the correct ngrok binary and auth token
ngrok_auth_token = os.getenv("NGROK_AUTHTOKEN")
ngrok.set_auth_token(ngrok_auth_token)

# Initializes your app with your bot token and signing secret
app = App(token=os.getenv('SLACK_BOT_TOKEN'),
          signing_secret=os.getenv('SLACK_SIGNING_SECRET'))


# Listens to incoming `/test-command` commands
@app.command("/test-command")
def handle_test_command(ack, respond):
  # Acknowledge the command request
  ack()
  # Respond with a message in the same channel
  respond("THIS IS A TESTING FOR THE BOT!")


if __name__ == "__main__":
  # Start ngrok tunnel
  ngrok_tunnel = ngrok.connect(3000)  # Assuming your app runs on port 3000
  print(f"ngrok URL: {ngrok_tunnel.public_url}")

  # Start your app
  app.start(port=3000)
