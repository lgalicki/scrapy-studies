-- URL: https://duckduckgo.com/

function main(splash, args)
  -- Faking the headers
  --[[headers = {
    ['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36"
  }
  splash:set_custom_headers(headers)]]--
  
  splash:on_request(function(request)
    request:set_header('User_Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36')
  end)
  
  -- Grabbing the URL and sending HTTP request
  url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))
  
  -- Writting text into the search box
  input_box = assert(splash:select("#search_form_input_homepage"))
  input_box:focus()
  input_box:send_text("my user agent")
  assert(splash:wait(1))
  
  -- Clicking on the search button to retrieve results
  --[[btn = assert(splash:select("#search_button_homepage"))
  btn:mouse_click()
  assert(splash:wait(2))]]--
  
  -- Pressing <Enter>
  input_box:send_keys("<Enter>")
  assert(splash:wait(2))
    
  -- Setting screen size to full
  splash:set_viewport_full()
  return {
    html = splash:html(),
    png = splash:png(),
  }
end