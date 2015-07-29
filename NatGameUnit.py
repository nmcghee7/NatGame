# Nat's Game 


	
class Unit(object):

	def __init__(
					self, Name=None, Photopath=None, Level=1, Experience=0,
					Strength=10, Stamina=10, Intelligence=10, MaxHealth=100, 
					CurrentHealth = 100, MaxMagic=100, CurrentMagic=100, 
					Defense=100, BaseMeleeDamage=1, AttackPower=100,
					MagicPower=100, Gold=0, Inventory=[]
					):
			
		self.Name = Name
		self.Level = Level
		self.Experience = Experience
		
		self.Strength = Strength
		self.Stamina = Stamina
		self.Intelligence = Intelligence
		
		self.MaxHealth = MaxHealth
		self.CurrentHealth = CurrentHealth
		self.MaxMagic = MaxMagic
		self.CurrentMagic = CurrentMagic
		self.Defense = Defense
		
		self.BaseMeleeDamage = BaseMeleeDamage
		self.AttackPower = AttackPower
		self.MagicPower = MagicPower
	
		self.Gold = Gold
		self.Inventory = []
		
	### Need to determine a method to automate wrong syntax error messages instead of typing out each one by hand.  
	### Unsure how to set check Inventory variable.  What kind of inputs will it actually take?
	

	
	@property		# Name Getter/Setter
	def Name(self):
		return self._Name
		
	@Name.setter
	def Name(self, value):
		self._Name = value
		
	@property		# Level Getter/Setter
	def Level(self):
		return self._Level
	
	@Level.setter	
	def Level(self, value):
		if isinstance(value, int):
			self._Level = value
		else:
			assert SyntaxError
			print "Invalid format for variable Level"
			quit()
		
	@property		# Experience Getter/Setter	
	def Experience(self):
		return self._Experience
	
	@Experience.setter
	def Experience(self, value):
		if isinstance(value, int):
			self._Experience = value
		else:
			assert SyntaxError
			print "Invalid format for variable EXPERIENCE"
			quit()
			
	@property		#Strength Getter/Setter
	def Strength(self):
		return self._Strength
		
	@Strength.setter
	def Strength(self, value):
		if isinstance(value, int):
			self._Strength = value
		else:
			assert SyntaxError
			print "Invalid format for variable STRENGTH"
			quit()
			
	@property		#Stamina Getter/Setter
	def Stamina(self):
		return self._Stamina
		
	@Stamina.setter
	def Stamina(self, value):
		if isinstance(value, int):
			self._Stamina = value
		else:
			assert SyntaxError
			print "Invalid format for variable STAMINA"
			quit()
		
	@property		#Intelligence Getter/Setter
	def Intelligence(self):
		return self._Intelligence
		
	@Intelligence.setter
	def Intelligence(self, value):
		if isinstance(value, int):
			self._Intelligence = value
		else:
			assert SyntaxError
			print "Invalid format for variable INTELLIGENCE"
			quit()
	
	@property		#MaxHealth Setter/Getter
	def MaxHealth(self):
		return self._MaxHealth
		
	@MaxHealth.setter
	def MaxHealth(self, value):
		if isinstance(value, int):
			self._MaxHealth = value
		else:
			assert SyntaxError
			print "Invalid format for variable MAXHEALTH"
			quit()
			
	@property		#Currenthealth getter/setter		
	def CurrentHealth(self):
		return self._CurrentHealth
		
	@CurrentHealth.setter
	def CurrentHealth(self, value):
		if isinstance(value, int):
			self._CurrentHealth = value
		else:
			assert SyntaxError
			print "Invalid format for variable CURRENTHEALTH"
			quit()
			
	@property	#MaxMagic Getter Setter
	def MaxMagic(self):
		return self._MaxMagic
		
	@MaxMagic.setter
	def MaxMagic(self, value):
		if isinstance(value, int):
			self._MaxMagic = value
		else:
			assert SyntaxError
			print "Invalid format for variable MaxMagic"
			quit()
			
	@property 			#Current Magic get/set
	def CurrentMagic(self):
		return self._CurrentMagic

	@CurrentMagic.setter
	def CurrentMagic(self, value):
		if isinstance(value, int):
			self._CurrentMagic = value
		else:
			assert SyntaxError
			print "Invalid format for variable CurrentMagic"
			quit()
			
	@property		#Defense Get/Setter	
	def Defense(self):
		return self._Defense
		
	@Defense.setter
	def Defense(self, value):
		if isinstance(value, int):
			self._Defense = value
		else:
			assert SyntaxError
			print "Invalid format for variable Defense"
			quit()
			
	@property		#Base Melee Damage get/set
	def BaseMeleeDamage(self):
		return self._BaseMeleeDamage
		
	@BaseMeleeDamage.setter	
	def BaseMeleeDamage(self, value):
		if isinstance(value, int):
			self._BaseMeleeDamage = value
		else:
			assert SyntaxError
			print "invalid format for variable BaseMeleeDamage"
			quit()
			
	@property			#AttackPower Get/Set 	
	def AttackPower(self):
		return self._AttackPower
	
	@AttackPower.setter
	def AttackPower(self, value):
		if isinstance(value, int):
			self._AttackPower = value
		else:
			assert SyntaxError
			print "invalid format for variable AttackPower"
			quit()
	
	@property		#MagicPower get/set
	def MagicPower(self):
		return self._MagicPower
		
	@MagicPower.setter
	def MagicPower(self, value):
		if isinstance(value, int):
			self._MagicPower = value
		else:
			assert SyntaxError
			print "invalid format for variable MagicPower"
			quit()
			
	
	@property			#Gold get/set
	def Gold(self):
		return self._Gold
		
	@Gold.setter
	def Gold(self, value):
		if isinstance(value, int):
			self._Gold = value
		else:
			assert SyntaxError
			print "Invalid format for variable Gold"
			quit()
	
	@property			# Inventory get/set
	def Inventory(self):
		return self._Inventory
		
	@Inventory.setter
	def Inventory(self, value):
		self._Inventory = value
	

	
class Player(Unit):

	def __init__(self, Armor=None, Weapon=None, Spell1=None, Spell2=None):
		
		super(Player, self).__init__()
		
		self.Name = "PlayerName"
		self.Photopath = "Natpic.gif"
		self.Armor = Armor
		self.Weapon = Weapon
		self.Spell1 = Spell1
		self.Spell2 = Spell2
	

		
	def GetWeapon():
		return self.Weapon
		
	def GetArmor():
		return self.Armor
		
	def GetSpell1():
		return self.armor
		
	def GetSpell2():
		return self.Spell2
