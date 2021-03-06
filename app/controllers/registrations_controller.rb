class RegistrationsController < Devise::RegistrationsController

  private

  def sign_up_params
    params.require(:user).permit(:email, :user_name, :password, :password_confirmation, :bio, :image_urls => [], :scores => [],
     :scoresstr => [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0].join(","))
  end

  def account_update_params
    params.require(:user).permit(:email, :user_name, :password, :password_confirmation, :current_password)
  end
end
