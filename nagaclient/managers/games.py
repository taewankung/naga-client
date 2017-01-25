
from .base import Manager

class GameManager(Manager):
    def __init__(self, client):
        super().__init__(client)
        if self.client.room.current_room:
            self.room_id = self.client.room.current_room['room_id']
            self.topic = 'naga/clients/{}/rooms/{}/update'.format(self.client.client_id,
                    self.room_id)

    def send_message(self, method, args, qos=0):
        request = dict(room_id=self.room_id, method=method, args=args)

        self.client.publish(self.topic, request, qos)

    def ready(self):
        args = dict()
        self.send_message('ready', args, 1)

    def initial(self):
        args = dict()
        self.send_message('initial', args, 1)

    def update(self, **kw):
        args = kw
        self.send_message('update', args, 0)

    #  def select_hero(self,hero_name='Sinsamut'):
        #  args = dict(hero_name = hero_name)
        #  self.send_message('select_hero',args,1)

    def move_hero(self, x, y, msg=""):
        args = dict(x=x, y=y,msg=msg)
        self.send_message('move_hero', args)

    def attack(self,target,msg=""):
        args = dict(target=target,msg=msg)
        self.send_message('attack',args)

    def buy_item(self, item, msg=""):
        args = dict(item=item,msg=msg)
        self.send_message('buy_item',args)

    def use_item(self, item, msg=""):
        args = dict(item=item,msg=msg)
        self.send_message('use_item',args)

    def upgrade_skill(self,skill_num,msg=""):
        args = dict(skill_num=skill_num,msg=msg)
        self.send_message('upgrade_skill',args)

    def stop(self):
        args = dict()
        self.send_message('stop',args)

    def use_skill(self,skill_num,target=None,msg=""):
        args = dict(skill_num=skill_num,target=target,msg=msg)
        self.send_message('use_skill',args)

    def skill_action(self, skill):
        args = dict(skill=skill)
        self.send_message('skill_action', args)

    def aliance_message(self,msg,args=dict()):
        args = dict(msg = msg,
                    args =args
                )
        self.send_message('aliance_message',args)
