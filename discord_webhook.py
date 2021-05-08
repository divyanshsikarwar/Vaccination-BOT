from discord_webhooks import DiscordWebhooks

# Go here to know how to get your Discord's Webhook Url : https://help.dashe.io/en/articles/2521940-how-to-create-a-discord-webhook-url
# Put your discord webhook url here.
webhook_url = ''


def send_msg(msg,vc):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='With Love from Divyansh Sikarwar')
    # main Content
    if(msg==0):
      webhook.set_content(title= msg,
                          description="Currently there are no Vaccination Centers available for your age in your area")
    elif(msg==-1):
      webhook.set_content(title= msg,
                          description="Sorry due to some techical reasons we cant access Vaccination Availability Info right now")
    else:
      webhook.set_content(title= "Vaccination Centers are now available !!",
                          description="Here is your Available Vaccination Center's list :Heart: :")
      # Appends a field
      for i in range(len(vc)):
        a=vc[i]
        print(a["name"],"(",a["min_age_limit"],"+) : ",a["available_capacity"])
        webhook.add_field(name ="Center Name", value=a["name"])
        webhook.add_field(name ="Min Age", value=a["min_age_limit"])
        webhook.add_field(name="Available Capacity", value=a["available_capacity"])
        webhook.add_field(name ="----", value="-----------------------------------")
        

    webhook.send()

    print("Report sent to discord")