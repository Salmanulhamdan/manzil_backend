from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser,HouseownerProfile,ProfessionalsProfile



@receiver(post_save, sender=CustomUser)
def create_profile(sender,instance,created, **kwargs):


    
 
    if created:
        if instance.usertype=='houseowner':
    
            HouseownerProfile.objects.create(user=instance)
            
        else:
           
            ProfessionalsProfile.objects.create(user=instance)
        
        # Add a default profile photo 
        if not instance.profile_photo:
            instance.profile_photo = "Profile_photos/default.jpg"
            instance.save()
            print(instance.profile_photo)


