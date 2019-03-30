# Telegram Core API client

It provides an example of how to interact with Telegram's Core API without being a bot.

The goal of this script is to reach a quick method to inspect and dump all available message information. Also to provide a quick way to kick and ban some suspect group participants.

Concretely, it renders a real Telegram client that:
- log in
- fetch a message from a group
- extract affected user information (of the previous message)
- iterates all group's participants list
  - inspects if affected user is a real participant
    - requests confirmation to ban it
  - review if current participant is a bot
    - requests confirmation to ban it

