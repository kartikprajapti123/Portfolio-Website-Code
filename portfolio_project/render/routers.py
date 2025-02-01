from rest_framework.routers import DefaultRouter
from user.views import UserViewSet,RegisterViewSet,OtpVierifyViewset,ResendOtpViewSet,LoginViewSet,ForgotPasswordViewSet,ResetPasswordViewSet,ChangePasswordViewSet,LoginWithGoogleViewSet
router=DefaultRouter()
from project.views import ProjectViewSet
from contact.views import ContactViewSet
from video_call.views import RoomViewSet,ChatMessageViewSet,ChatRoomViewSet


router.register("user",UserViewSet,basename="user")
router.register("register",RegisterViewSet,basename="register")

router.register("verify-otp",OtpVierifyViewset,basename="verify-otp")
router.register("resend-otp",ResendOtpViewSet,basename="resend-otp")
router.register("login",LoginViewSet,basename="login")
router.register("forgot-password",ForgotPasswordViewSet,basename="forgot-password")
router.register("reset-password",ResetPasswordViewSet,basename="reset-password")
router.register("change-password",ChangePasswordViewSet,basename="change-password")
router.register("google-authentication",LoginWithGoogleViewSet,basename="google-authentication")
router.register("project",ProjectViewSet,basename="project")
router.register("contact-us",ContactViewSet,basename="contact-us")
router.register("video-call-room",RoomViewSet,basename="room")


router.register("chat-room",ChatRoomViewSet,basename="chatroom")
router.register("chat-message",ChatMessageViewSet,basename="chatmessage")








