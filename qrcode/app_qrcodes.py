import qrcode

"""image = qrcode.make('https://www.instagram.com/icejardimdasoliveiras/')
image.save('qrcode_insta.png')"""

links_icejo = {
    'Instagram': 'https://www.instagram.com/icejardimdasoliveiras/',
    'YouTube': 'https://www.youtube.com/channel/UCFSi8Zlbtq_BraBBog-j-pw'
}

for rede_soci in links_icejo:
    link = (links_icejo[rede_soci])
    image = qrcode.make(link)
    image.save(f'qr_code_{rede_soci}.png')
