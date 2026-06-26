from django.core.management.base import BaseCommand
from home.models import Guitar

class Command(BaseCommand):
    help = 'Seeds the database with premium guitars and accessories'

    def handle(self, *args, **options):
        # Clear existing data first
        Guitar.objects.all().delete()
        
        guitars_data = [
            # Acoustic Guitars
            {
                'name': 'Yamaha FS80C Acoustic',
                'brand': 'Yamaha',
                'price': 9490,
                'image': 'https://images.unsplash.com/photo-1565075772172-5a232b7d5008?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Yamaha+FS80C',
                'flipkart_link': 'https://www.flipkart.com/search?q=Yamaha+FS80C'
            },
            {
                'name': 'Kadence Frontier Series',
                'brand': 'Kadence',
                'price': 4999,
                'image': 'https://images.unsplash.com/photo-1510915361894-db8b60106cb1?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Kadence+Frontier',
                'flipkart_link': 'https://www.flipkart.com/search?q=Kadence+Frontier'
            },
            {
                'name': 'Fender CD-60S Acoustic',
                'brand': 'Fender',
                'price': 18999,
                'image': 'https://images.unsplash.com/photo-1760413209533-c65c9e6b538f?guitarsw=800&auto=format&fit=crop&q=80',
                'amazon_link': 'https://www.amazon.in/s?k=Fender+CD-60S',
                'flipkart_link': 'https://www.flipkart.com/search?q=Fender+CD-60S'
            },
            {
                'name': 'Ibanez MD39C Acoustic',
                'brand': 'Ibanez',
                'price': 7649,
                'image': 'https://images.unsplash.com/photo-1485698357635-ebb21ec52773?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Ibanez+MD39C',
                'flipkart_link': 'https://www.flipkart.com/search?q=Ibanez+MD39C'
            },
            # Electric Guitars
            {
                'name': 'Fender Player Stratocaster',
                'brand': 'Fender',
                'price': 68999,
                'image': 'https://images.unsplash.com/photo-1563357989-f6cdbbae76cb?guitarsw=800&auto=format&fit=crop&q=80',
                'amazon_link': 'https://www.amazon.in/s?k=Fender+Player+Stratocaster',
                'flipkart_link': 'https://www.flipkart.com/search?q=Fender+Player+Stratocaster'
            },
            {
                'name': 'Epiphone Les Paul Express',
                'brand': 'Epiphone',
                'price': 15490,
                'image': 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Epiphone+Les+Paul+Express',
                'flipkart_link': 'https://www.flipkart.com/search?q=Epiphone+Les+Paul+Express'
            },
            {
                'name': 'Ibanez GRG170DX Electric',
                'brand': 'Ibanez',
                'price': 18290,
                'image': 'https://images.unsplash.com/photo-1525201548982-be346cae528f?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Ibanez+GRG170DX',
                'flipkart_link': 'https://www.flipkart.com/search?q=Ibanez+GRG170DX'
            },
            {
                'name': 'Jackson JS11 Dinky',
                'brand': 'Jackson',
                'price': 14999,
                'image': 'https://images.unsplash.com/photo-1516924962500-2b4b3b99ea02?w=500&auto=format&fit=crop&q=60',
                'amazon_link': 'https://www.amazon.in/s?k=Jackson+JS11+Dinky',
                'flipkart_link': 'https://www.flipkart.com/search?q=Jackson+JS11+Dinky'
            },
            # Bass Guitars
            {
                'name': 'Fender Precision Bass',
                'brand': 'Fender',
                'price': 68999,
                'image': 'https://images.unsplash.com/photo-1564186763535-ebb21ec52773?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Fender+Precision+Bass',
                'flipkart_link': 'https://www.flipkart.com/search?q=Fender+Precision+Bass'
            },
            {
                'name': 'Ibanez GSR200 Bass',
                'brand': 'Ibanez',
                'price': 19999,
                'image': 'https://images.unsplash.com/photo-1583763788274-5b3ccd04e675?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Ibanez+GSR200',
                'flipkart_link': 'https://www.flipkart.com/search?q=Ibanez+GSR200'
            },
            {
                'name': 'Yamaha TRBX174 Bass',
                'brand': 'Yamaha',
                'price': 17490,
                'image': 'https://images.unsplash.com/photo-1619118742514-411a76c66cf1?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Yamaha+TRBX174',
                'flipkart_link': 'https://www.flipkart.com/search?q=Yamaha+TRBX174'
            },
            {
                'name': 'Cort Action Bass V',
                'brand': 'Cort',
                'price': 21999,
                'image': 'https://media.istockphoto.com/id/651209608/photo/close-up-photo-of-bass-guitar-player.webp?a=1&b=1&s=612x612&w=0&k=20&c=6DuhU1lOT634QCiO8YHwXk_o6MxN1e6jqPtlf1QJd4g=',
                'amazon_link': 'https://www.amazon.in/s?k=Cort+Action+Bass+V',
                'flipkart_link': 'https://www.flipkart.com/search?q=Cort+Action+Bass+V'
            },
            # Ukuleles
            {
                'name': 'Kala KA-15S Soprano Ukulele',
                'brand': 'Kala',
                'price': 4890,
                'image': 'https://images.unsplash.com/photo-1624247079844-d306e0157dbb?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Kala+KA-15S+Ukulele',
                'flipkart_link': 'https://www.flipkart.com/search?q=Kala+KA-15S+Ukulele'
            },
            {
                'name': 'Flight Concert Ukulele',
                'brand': 'Flight',
                'price': 5999,
                'image': 'https://images.unsplash.com/photo-1507838153414-b4b713384a76?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Flight+Concert+Ukulele',
                'flipkart_link': 'https://www.flipkart.com/search?q=Flight+Concert+Ukulele'
            },
            {
                'name': 'Cordoba 15CM Concert Ukulele',
                'brand': 'Cordoba',
                'price': 8499,
                'image': 'https://images.unsplash.com/photo-1603048588665-791ca8aea617?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Cordoba+15CM',
                'flipkart_link': 'https://www.flipkart.com/search?q=Cordoba+15CM'
            },
            {
                'name': 'Kadence Wanderer Tenor Ukulele',
                'brand': 'Kadence',
                'price': 3499,
                'image': 'https://images.unsplash.com/photo-1624247079844-d306e0157dbb?w=500&auto=format&fit=crop&q=60',
                'amazon_link': 'https://www.amazon.in/s?k=Kadence+Wanderer+Ukulele',
                'flipkart_link': 'https://www.flipkart.com/search?q=Kadence+Wanderer+Ukulele'
            },
            # Accessories - Covers
            {
                'name': 'Gator Cases Gig Bag',
                'brand': 'Gator',
                'price': 3499,
                'image': 'https://images.unsplash.com/photo-1568193755639-966996b79a9a?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Gator+Cases+Guitar+Bag',
                'flipkart_link': 'https://www.flipkart.com/search?q=Gator+Cases+Guitar+Bag'
            },
            {
                'name': 'Mono M80 Sleeve Premium Case',
                'brand': 'Mono',
                'price': 18999,
                'image': 'https://images.unsplash.com/photo-1601049676099-e7ed07d825b0?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Mono+M80+Guitar+Bag',
                'flipkart_link': 'https://www.flipkart.com/search?q=Mono+M80+Guitar+Bag'
            },
            {
                'name': 'Road Runner Boulevard Gig Bag',
                'brand': 'Road Runner',
                'price': 7499,
                'image': 'https://images.unsplash.com/photo-1568193755639-966996b79a9a?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Road+Runner+Guitar+Bag',
                'flipkart_link': 'https://www.flipkart.com/search?q=Road+Runner+Guitar+Bag'
            },
            {
                'name': 'Juarez Padded Guitar Bag',
                'brand': 'Juarez',
                'price': 999,
                'image': 'https://images.unsplash.com/photo-1568193755639-966996b79a9a?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Juarez+Padded+Guitar+Bag',
                'flipkart_link': 'https://www.flipkart.com/search?q=Juarez+Padded+Guitar+Bag'
            },
            # Accessories - Straps
            {
                'name': 'Fender Monogrammed Strap',
                'brand': 'Fender',
                'price': 1299,
                'image': 'https://images.unsplash.com/photo-1599302863963-5da550e24adf?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Fender+Monogrammed+Strap',
                'flipkart_link': 'https://www.flipkart.com/search?q=Fender+Monogrammed+Strap'
            },
            {
                'name': 'Levy\'s Leathers Suede Strap',
                'brand': 'Levy\'s',
                'price': 3999,
                'image': 'https://images.unsplash.com/photo-1599302863963-5da550e24adf?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Levys+Leathers+Suede+Strap',
                'flipkart_link': 'https://www.flipkart.com/search?q=Levys+Leathers+Suede+Strap'
            },
            {
                'name': 'D\'Addario Woven Strap',
                'brand': 'D\'Addario',
                'price': 899,
                'image': 'https://images.unsplash.com/photo-1599302863963-5da550e24adf?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=DAddario+Woven+Strap',
                'flipkart_link': 'https://www.flipkart.com/search?q=DAddario+Woven+Strap'
            },
            {
                'name': 'Ernie Ball Polypro Strap',
                'brand': 'Ernie Ball',
                'price': 699,
                'image': 'https://images.unsplash.com/photo-1599302863963-5da550e24adf?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Ernie+Ball+Polypro+Strap',
                'flipkart_link': 'https://www.flipkart.com/search?q=Ernie+Ball+Polypro+Strap'
            },
            # Accessories - Amplifiers
            {
                'name': 'Marshall MG10 Gold',
                'brand': 'Marshall',
                'price': 7499,
                'image': 'https://images.unsplash.com/photo-1557855684-8aa6f40997df?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Marshall+MG10+Amplifier',
                'flipkart_link': 'https://www.flipkart.com/search?q=Marshall+MG10+Amplifier'
            },
            {
                'name': 'Fender Champion 20',
                'brand': 'Fender',
                'price': 11999,
                'image': 'https://images.unsplash.com/photo-1598518141892-06ba05f87bbe?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Fender+Champion+20',
                'flipkart_link': 'https://www.flipkart.com/search?q=Fender+Champion+20'
            },
            {
                'name': 'Vox Pathfinder 10',
                'brand': 'Vox',
                'price': 8499,
                'image': 'https://images.unsplash.com/photo-1550985616-10810253b84d?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Vox+Pathfinder+10',
                'flipkart_link': 'https://www.flipkart.com/search?q=Vox+Pathfinder+10'
            },
            {
                'name': 'Cort CM15R Guitar Amp',
                'brand': 'Cort',
                'price': 6499,
                'image': 'https://images.unsplash.com/photo-1557855684-8aa6f40997df?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Cort+CM15R+Amplifier',
                'flipkart_link': 'https://www.flipkart.com/search?q=Cort+CM15R+Amplifier'
            },
            # Accessories - Picks/Strings
            {
                'name': 'Ernie Ball Slinky Strings',
                'brand': 'Ernie Ball',
                'price': 650,
                'image': 'https://images.unsplash.com/photo-1636800874844-fda5deef5b05?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Ernie+Ball+Slinky+Strings',
                'flipkart_link': 'https://www.flipkart.com/search?q=Ernie+Ball+Slinky+Strings'
            },
            {
                'name': 'Dunlop Tortex Picks 12-pack',
                'brand': 'Dunlop',
                'price': 499,
                'image': 'https://images.unsplash.com/photo-1636800874844-fda5deef5b05?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Dunlop+Tortex+Picks',
                'flipkart_link': 'https://www.flipkart.com/search?q=Dunlop+Tortex+Picks'
            },
            {
                'name': 'D\'Addario EJ16 Strings',
                'brand': 'D\'Addario',
                'price': 750,
                'image': 'https://images.unsplash.com/photo-1636800874844-fda5deef5b05?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=DAddario+EJ16+Strings',
                'flipkart_link': 'https://www.flipkart.com/search?q=DAddario+EJ16+Strings'
            },
            {
                'name': 'Fender Classic Picks 12-pack',
                'brand': 'Fender',
                'price': 399,
                'image': 'https://images.unsplash.com/photo-1636800874844-fda5deef5b05?w=500',
                'amazon_link': 'https://www.amazon.in/s?k=Fender+Classic+Picks',
                'flipkart_link': 'https://www.flipkart.com/search?q=Fender+Classic+Picks'
            }
        ]

        created_count = 0
        for guitar_item in guitars_data:
            Guitar.objects.get_or_create(
                name=guitar_item['name'],
                brand=guitar_item['brand'],
                price=guitar_item['price'],
                image=guitar_item['image'],
                amazon_link=guitar_item['amazon_link'],
                flipkart_link=guitar_item['flipkart_link']
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} products in the database!'))
