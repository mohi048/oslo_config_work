from oslo.config import cfg #importing cfg module

print "Listing out the current configuration"
for k, v in cfg.CONF.iteritems():
    print k,v
print "Listing complete"

# Since we do not have the conf file , we are using the default values over here

print "Registering param api_server with local ip"
myconfig = [cfg.StrOpt('api_server_ip', default='127.0.0.1', help="This is api server ip"),] #initializing the configuration string
cfg.CONF.register_opts(myconfig) # registering the string

print "Checking out the configuration"
for k, v in cfg.CONF.iteritems():
    print k,v
print "Listing complete"


print "Clearing out the configuration"
cfg.CONF.unregister_opts(myconfig) # un-registering the configuration

######################################################################################

print "Registering mutiple parameters now"
mymultipleconfig = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on.'),
    cfg.Opt('bind_port',
            default='9292',
            help='Port number to listen on.')
		]

cfg.CONF.register_opts(mymultipleconfig) # registering the multiple configurations


print "Checking out the configuration"
for k, v in cfg.CONF.iteritems():
    print k,v
print "Listing complete"

cfg.CONF.unregister_opts(mymultipleconfig) # un-registering the configuration

print "Registering DICTIONARY parameters now"

mydict = {'ip':'v4','class':'A'}
mynewconfig = [cfg.DictOpt('myconfig', default=mydict, help='this is my help'),] # initializing the configuration string
cfg.CONF.register_opts(mynewconfig) # registering the configuration

for k, v in cfg.CONF.iteritems():
    print k,v
print "Listing complete"
