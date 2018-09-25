RichPresenceDiscord <- function(){
  folder <- rstudioapi::getActiveProject()
  system(sprintf("python R/main.py %s" , folder))

}
