-- URL: https://www.livecoin.net/en

function main(splash, args)
  -- Faking the headers
  splash:on_request(function(request)
    request:set_header('User_Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36')
  end)
  
  -- Disabling Splash's default incognito mode
  splash.private_mode_enabled = false
  
  -- Grabbing the URL and sending HTTP request
  url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))

  -- Clicking on the fifth tab (RUR)
  rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
  rur_tab[5]:mouse_click()
  assert(splash:wait(5))
  
  -- Setting screen size to full
  splash:set_viewport_full()
  return {
    html = splash:html(),
    png = splash:png(),
  }
end