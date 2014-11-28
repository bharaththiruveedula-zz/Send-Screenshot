import gtk.gdk
import json
import subprocess

API_KEY = <API KEY>
w = gtk.gdk.get_default_root_window()
sz = w.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
pb.save("screenshot.png","png")
#Upload the image
data = json.loads(subprocess.check_output(['curl','-u', str(API_KEY)+':', '-d', 'file_name=screenshot.png', '-d', 'file_type=image/png','-X','POST', 'https://api.pushbullet.com/v2/upload-request ']))
print data

file_url =  data['file_url']
upload_url = data['upload_url']
file_name = data['file_name']
awsaccesskeyid = data['data']['awsaccesskeyid']
key = data['data']['key']
signature = data['data']['signature']
policy = data['data']['policy']

print subprocess.check_output(['curl', '-F','awsaccesskeyid='+awsaccesskeyid, '-F','acl=public-read','-F','key='+key, '-F', 'signature='+signature,'-F', 'policy='+policy,'-F','content-type=image/png', '-F', 'file=@screenshot.png','-i', '-X','POST',upload_url])
print subprocess.check_output(['curl','-u', str(API_KEY)+':', '-d', 'device_iden=<device iden>','-d','type=file','-d','file_name='+file_name,'-d','file_url='+file_url,'-d', 'file_type=image/png','-X','POST','https://api.pushbullet.com/api/pushes'])



