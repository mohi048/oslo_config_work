from oslo_config import cfg

my_group = cfg.OptGroup(name='simple',title='A Simple Example')

config1 = [cfg.BoolOpt('enable', default=False, help=('Boolean text type'))]
config2 = [cfg.StrOpt('message', default='mydefault', help=('this is text type'))]
config3 = [cfg.IntOpt('value', default=30, help=('this is integer type'))]

cfg.CONF.register_group(my_group)
cfg.CONF.register_opts(config1, my_group)
cfg.CONF.register_opts(config2, my_group)
cfg.CONF.register_opts(config3, my_group)
cfg.CONF(default_config_files=['app.conf'])

print cfg.CONF.simple.enable
print cfg.CONF.simple.message
print cfg.CONF.simple.value
