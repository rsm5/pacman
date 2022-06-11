# coding=utf-8
# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
	"""
		A reflex agent chooses an action at each choice point by examining
		its alternatives via a state evaluation function.

		The code below is provided as a guide.  You are welcome to change
		it in any way you see fit, so long as you don't touch our method
		headers.
	"""

	def getAction(self, gameState):
		"""
		You do not need to change this method, but you're welcome to.

		getAction chooses among the best options according to the evaluation function.

		Just like in the previous project, getAction takes a GameState and returns
		some Directions.X for some X in the set {North, South, West, East, Stop}
		"""
		# Collect legal moves and successor states
		legalMoves = gameState.getLegalActions()

		# Choose one of the best actions
		scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		"Add more of your code here if you want to"

		return legalMoves[chosenIndex]

	def evaluationFunction(self, currentGameState, action):
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()

		#ghostPositions = successorGameState.getGhostPositions()

		newGhostStates = successorGameState.getGhostStates()
		newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
		legalMoves = currentGameState.getLegalActions()

		"*** YOUR CODE HERE ***"

		closestGhostIsScared = newGhostStates[0].scaredTimer > 0

		closestGhostPosition = newGhostStates[0].configuration.pos
		print('closestGhostPosition...', closestGhostPosition)

		#closestGhostPosition = successorGameState.getGhostPosition(0)

		#Não estamos utilizando o "closestGhost", logo, ele foi comentado.
		#closestGhost = manhattanDistance(newPos, closestGhostPosition)
		#print('closestGhost...', closestGhost)

		newFoodPositions = newFood.asList()
		foodDistances = [manhattanDistance(newPos, foodPosition) for foodPosition in newFoodPositions]

		print('newFoodPositions...', newFoodPositions)
		print('foodDistances...', foodDistances)

		ghostListPosition = [ghostState.configuration.pos for ghostState in newGhostStates]
		ghostDistances = [manhattanDistance(newPos, ghostPosition) for ghostPosition in ghostListPosition]

		print('ghostListPosition...', ghostListPosition)
		print('ghostDistances...', ghostDistances)

		#ghostDistances = [manhattanDistance(newPos, ghostPosition) for ghostPosition in ghostPositions]


		#max([manhattanDistance(ghostListPosition, foodPosition) for foodPosition in newFoodPositions])

		# Select best actions given the state
		#distancesToGhost = [manhattanDistance( pos, closestGhostPosition ) for pos in newPositions]



		# Fantasma Não Assustado:
				# -> Direção em que a comida está próxima dele, porém o mais distante do fantasma
		# ELSE
				# -> Direção em que a comida está próxima dele.

		if not closestGhostIsScared:
			# movimentar-se para a comida mais próxima do pacman e mais longe do fantasma mais próximo
			bestScore = [0,0] #AVALIAR!!!!

			for foodPosition in newFoodPositions:
				print('foodPosition...', foodPosition)

				if(successorGameState.hasFood(foodPosition[0], foodPosition[1])):
					bestScore = max([manhattanDistance(closestGhostPosition, foodPosition)])

			#if(not successorGameState.isWin()):
			#	bestScore = max([manhattanDistance(closestGhostPosition, foodPosition) for foodPosition in newFoodPositions])
			#else:
			#	bestScore = foodDistances[0]




			#bestScore = ([manhattanDistance(closestGhostPosition, foodPosition) for foodPosition in newFoodPositions])

			#if (successorGameState.hasFood(bestScore)):
			#	successorGameState.isWin()

		else:
			bestScore = min( foodDistances )
			#bestProb = self.prob_attack

		#bestActions = [action for action, distance in zip( legalMoves, ghostDistances ) if distance == bestScore and (not successorGameState.isWin())]
		bestActions = [action for action, distance in zip( legalMoves, ghostDistances ) if distance == bestScore]


		# Atrás da comida
		# Correr do fantasma no sentido oposto

		# Calcular distância para a comida
		#newFoodPositions = newFood.asList()
		#foodDistances = [manhattanDistance(newPos, foodPosition) for foodPosition in newFoodPositions]

		# Calcular distância para o fantasma

		return successorGameState.getScore()

	"""
				Pra testar a implementação que vc colocar os seguintes comandos:
				- python pacman.py -p ReflexAgent -l testClassic

				Deste jeito vc roda só com um fantasminha, mas no ambiente do jogo:
				- python pacman.py --frameTime 0.1 -p ReflexAgent -k 1

				Deste jeito vc roda só com dois fantasminhas, mas no ambiente do jogo:
				- python pacman.py --frameTime 0.1 -p ReflexAgent -k 2

				E aqui vc roda a "prova".
				- python autograder.py -q q1
			"""

	"""

		# Useful information you can extract from a GameState (pacman.py)
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()
		newGhostStates = successorGameState.getGhostStates()
		newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

		"*** YOUR CODE HERE ***"
		score = 0

		closestGhostPosition = newGhostStates[0].configuration.pos
		closestGhost = manhattanDistance(newPos, closestGhostPosition)

				"*** ghostListPosition = [ghostState.configuration.pos for ghostState in newGhostStates] ***"
				"*** ghostDistances = [manhattanDistance(newPos, ghostListPosition) for ghostPosition in ghostListPosition] ***"

		# Minimize distance from pacman to food
		newFoodPositions = newFood.asList()
		foodDistances = [manhattanDistance(newPos, foodPosition) for foodPosition in newFoodPositions]

		if len(foodDistances) == 0:
			return 0

		closestFood = min(foodDistances)

		# Stop action would reduce score because of the pacman's timer constraint
		if action == 'Stop':
			score -= 50

		return successorGameState.getScore() + closestGhost / (closestFood * 10) + score

	"""


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

