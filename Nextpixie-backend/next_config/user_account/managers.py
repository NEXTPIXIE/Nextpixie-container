from django.contrib.auth.base_user import BaseUserManager







class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        user=self._create_user(email, password, is_staff=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, is_admin=True, is_staff=True, is_superuser=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_admin(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, is_admin=True, is_staff=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        
        return user

