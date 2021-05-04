from discord_webhooks import DiscordWebhooks

#Put your discord webhook url here.

webhook_url = 'https://discord.com/api/webhooks/839177348963762258/32XBE1k6TYC0omH8VOuIti3HBkVsWsAaiC1q1Kifo46DfGzzJQEBIBb4XLynAFw0ZyOt'


def send_msg(msg,vaccine_centers):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- Divyansh Sikarwar')
    # main Content
    if(len(vaccine_centers)==0):
      webhook.set_content(title= msg,
                          description="Currently there are no Vaccination Centers available for your age in your area")
    else:
      webhook.set_content(title= "Vaccination Centers are now available !!",
                          description="Here is your Available Vaccination Center's list with love :Heart: :")
      # Appends a field
      for center in vaccine_centers:
        
        webhook.add_field(name ="Center Name", value=center[0])
        webhook.add_field(name ="Address", value=center[1])
        webhook.add_field(name="-", value="--------")
        

    webhook.send()

    print("Report sent to discord")