class Recorded:

	def __init__( self ):
		self.type = -1
		self.mediaFilename = None
		self.thumbFilename = None
		self.time = None
		self.photographer = None
		self.name = None
		self.tags = []
		self.colorStroke = None
		self.colorFill = None
		self.hashKey = None

		#transient
		self.media = None
		self.thumb = None