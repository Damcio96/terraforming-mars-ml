from action_type import ActionType
from enum import Enum

class ActionGroup(Enum):
    TURN = 1
    CONVERSION = 2
    MILESTONES = 3
    AWARDS = 4
    STANDARD_PROJECT = 5
    CARD_PLAY = 6
    CARD_ACTION = 7

ACTION_GROUP = {
    ActionType.PASS: ActionGroup.TURN,
    ActionType.WAIT: ActionGroup.TURN,

    ActionType.HEAT_INTO_TEMPERATURE: ActionGroup.CONVERSION,
    ActionType.PLANTS_INTO_GREENERY: ActionGroup.CONVERSION,

    ActionType.SELL_PATENTS: ActionGroup.STANDARD_PROJECT,
    ActionType.POWER_PLANT: ActionGroup.STANDARD_PROJECT,
    ActionType.ASTEROID: ActionGroup.STANDARD_PROJECT,
    ActionType.AQUIFER: ActionGroup.STANDARD_PROJECT,
    ActionType.GREENERY: ActionGroup.STANDARD_PROJECT,
    ActionType.CITY: ActionGroup.STANDARD_PROJECT,

    ActionType.CLAIM_TERRAFORMER: ActionGroup.MILESTONES,
    ActionType.CLAIM_MAYOR: ActionGroup.MILESTONES,
    ActionType.CLAIM_GARDENER: ActionGroup.MILESTONES,
    ActionType.CLAIM_BUILDER: ActionGroup.MILESTONES,
    ActionType.CLAIM_PLANNER: ActionGroup.MILESTONES,

    ActionType.FUND_LANDLORD: ActionGroup.AWARDS,
    ActionType.FUND_BANKER: ActionGroup.AWARDS,
    ActionType.FUND_SCIENTIST: ActionGroup.AWARDS,
    ActionType.FUND_THERMALIST: ActionGroup.AWARDS,
    ActionType.FUND_MINER: ActionGroup.AWARDS,

    # ActionType.PLAY_CARD_SLOT_0: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_1: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_2: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_3: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_4: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_5: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_6: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_7: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_8: ActionGroup.CARD_PLAY,
    # ActionType.PLAY_CARD_SLOT_9: ActionGroup.CARD_PLAY,

    # ActionType.PLAY_CARD_ACTION_0: ActionGroup.CARD_ACTION,
    # ActionType.PLAY_CARD_ACTION_1: ActionGroup.CARD_ACTION,
    # ActionType.PLAY_CARD_ACTION_2: ActionGroup.CARD_ACTION,
    # ActionType.PLAY_CARD_ACTION_3: ActionGroup.CARD_ACTION,
    # ActionType.PLAY_CARD_ACTION_4: ActionGroup.CARD_ACTION,

}