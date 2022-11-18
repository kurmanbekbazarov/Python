from admin import Admin

mod = Admin('den', 'kuso', privileges=['can ban users', 'can mute users', 'can unfollow users'])

mod.show_privileges()