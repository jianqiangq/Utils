import base64
 
for index in range(10):
    with open("images/{0}.jpg".format(str(index + 1)), 'rb') as f:
        base64_data = base64.b64encode(f.read())
        print(base64_data)

        with open("images/base64_{}.txt".format(str(index + 1)), 'wb') as f:
            f.write(base64_data)
