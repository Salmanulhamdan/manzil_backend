from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser,HouseownerProfile,ProfessionalsProfile,UserPlan
from django.db.models.signals import pre_save
from django.utils import timezone



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
           






@receiver(pre_save, sender=UserPlan)
def check_end_date(sender, instance, **kwargs):
    if instance.end_date and instance.end_date < timezone.now():
        
        instance.delete()

        if instance.user.usertype=='houseowner':
            profile=HouseownerProfile.objects.get(user=instance.user)
            profile.upgraded=False
            profile.save()
           
        else:
            profile=ProfessionalsProfile.objects.get(user=instance.user)
            profile.upgraded=False
            profile.save()
            


    

