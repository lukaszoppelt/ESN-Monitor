from discord_webhook import DiscordWebhook, DiscordEmbed


webhook = DiscordWebhook(url='https://discord.com/api/webhooks/969297246787092490/6q8E_HBXhXcYv6qEJ6pdrUmZ9Xq18BJu1tD-lHYKZ8i6ZpL6ymyh-xTgtDntPA6UlzMA', username="Fitnesslord")

def sendhook(product, url1, img):
    embed = DiscordEmbed(title='BACK IN STOCK', description=url1, color='03b2f8')
    embed.set_author(name=product, url=url1)
    embed.set_footer(text='BACK IN STOCK')
    embed.set_timestamp()
    embed.set_thumbnail(url=img)
    #embed.add_embed_field(name='Field 1', value='Lorem ipsum')
    #embed.add_embed_field(name='Field 2', value='dolor sit')
    #embed.add_embed_field(name='Field 3', value='amet consetetur')
    #embed.add_embed_field(name='Field 4', value='sadipscing elitr')

    webhook.add_embed(embed)
    response = webhook.execute()