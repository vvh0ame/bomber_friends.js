import requests

class BomberFriends:
	def __init__(self) -> None:
		self.api = "https://e1e6.playfabapi.com"
		self.headers = {
			"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
			"x-playfabsdk": "Cocos2d-xSDK-0.40.180529",
			"content-type": "application/json",
			"connection": "keep_alive"
		}
		self.user_id = None
		self.title_id = "E1E6"
		self.entity_token = None
		self.session_ticket = None
		
	def login_with_custom_id(
			self,
			custom_id: str,
			create_account: bool = True) -> dict:
		data = {
			"CreateAccount": create_account,
			"CustomId": custom_id,
			"TitleId": self.title_id
		}
		response = requests.post(
			f"{self.api}/Client/LoginWithCustomID",
			json=data,
			headers=self.headers).json()
		if "SessionTicket" in response["data"]:
			self.custom_id = custom_id
			self.user_id = response["data"]["PlayFabId"]
			self.session_ticket = response["data"]["SessionTicket"]
			self.entity_token = response["data"]["EntityToken"]["EntityToken"]
			self.headers["x-authorization"] = self.session_ticket
			self.headers["x-entitytoken"] = self.entity_token
		return response

	def get_entity_token(self) -> dict:
		return requests.post(
			f"{self.api}/Authentication/GetEntityToken",
			headers=self.headers).json()

	def get_title_data(
			self,
			keys: list = ["ScriptVersionAndroid"]) -> dict:
		data = {
			"Keys": keys
		}
		return requests.post(
			f"{self.api}/Client/GetTitleData",
			json=data,
			headers=self.headers).json()

	def get_server_status(
			self,
			platform: str = "android",
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "getServerStatus",
			"FunctionParameter": {
				"platform": platform
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def update_display_name(self, display_name: str) -> dict:
		data = {
			"DisplayName": display_name
		}
		return requests.post(
			f"{self.api}/Client/UpdateUserTitleDisplayName",
			json=data,
			headers=self.headers).json()

	def get_leaderboard(
			self,
			max_results_count: int = 100,
			start_position: int = 0,
			statistic_name: str = "Trophies",
			show_avatar_url: bool = False,
			show_banned_until: bool = False,
			show_campaign_attributions: bool = False,
			show_contact_email_addresses: bool = False,
			show_created: bool = False,
			show_display_name: bool = True,
			show_last_login: bool = False,
			show_linked_accounts: bool = False,
			show_locations: bool = False,
			show_memberships: bool = False,
			show_origiation: bool = False,
			show_push_notification_registrations: bool = False,
			show_statistics: bool = False,
			show_tags: bool = True,
			show_total_value_to_data_in_usd: bool = False,
			show_values_to_date: bool = False) -> dict:
		data = {
			"MaxResultsCount": max_results_count,
			"ProfileConstraints": {
				"ShowAvatarUrl": show_avatar_url,
				"ShowBannedUntil": show_banned_until,
				"ShowCampaignAttributions": show_campaign_attributions,
				"ShowContactEmailAddresses": show_contact_email_addresses,
				"ShowCreated": show_created,
				"ShowDisplayName": show_display_name,
    			"ShowLastLogin": show_last_login,
    			"ShowLinkedAccounts": show_linked_accounts,
    			"ShowLocations": show_locations,
    			"ShowMemberships": show_memberships,
    			"ShowOrigination": show_origiation,
    			"ShowPushNotificationRegistrations": show_push_notification_registrations,
    			"ShowStatistics": show_statistics,
    			"ShowTags": show_tags,
    			"ShowTotalValueToDateInUsd": show_total_value_to_data_in_usd,
    			"ShowValuesToDate": show_values_to_date
			},
			"StartPosition": start_position,
			"StatisticName": statistic_name
		}
		return requests.post(
			f"{self.api}/Client/GetLeaderboard",
			json=data,
			headers=self.headers).json()

	def claim_season_prize(
			self,
			name: str,
			id: int = 0,
			is_free: bool = True,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "claimSeasonPrize",
			"FunctionParameter": {
				"id": id,
				"isFree": is_free,
				"name": name
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def get_initial_data(
			self,
			version: int = 756,
			platform: str = "android",
			pd_datas: list = ["deckslots", "dungeonrundata", "testidata"],
			rod_datas: list = ["_clandata"],
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "getInitialData",
			"FunctionParameter": {
				"version": version,
				"platform": platform,
				"pddatas": pd_datas,
				"roddatas": rod_datas
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def claim_reward(
			self,
			id: int = 0,
			reward_spin: bool = False,
			name: str = "wheel"	,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "claimReward",
			"FunctionParameter": {
				"id": id,
				"reward_spin": reward_spin,
				"name": name
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def get_single_player_reward(
			self,
			level: int,
			type: int = 0,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "getSinglePlayerReward",
			"FunctionParameter": {
				"level": level,
				"type": 0
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def save_bomber_user_data(
			self,
			data: str,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "saveBomberUserData",
			"FunctionParameter": {
				"data": data,
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def start_opening_slot(
			self,
			slot: int,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "tryStartOpeningSlotChest",
			"FunctionParameter": {
				"Slot": slot
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def open_slot(
			self,
			slot: int,
			cost: int = 0,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "tryStartOpeningSlotChest",
			"FunctionParameter": {
				"Slot": slot,
				"cost": cost
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def update_user_data(
			self,
			data: dict,
			permission: str = "Private") -> dict:
		data = {
			"Data": data,
			"Permission": permission
		}
		return requests.post(
			f"{self.api}/Client/UpdateUserData",
			json=data,
			headers=self.headers).json()

	def tutorial_won(
			self,
			standing: int = 0,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "tutorialWon",
			"FunctionParameter": {
				"standing": standing
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()

	def add_fashion_points(
			self,
			points: int,
			ad: bool = False,
			generate_play_stream_event: bool = False,
			revision_selection: str = "Live") -> dict:
		data = {
			"FunctionName": "addFashionPoints",
			"FunctionParameter": {
				"points": points,
				"ad": ad
			},
			"GeneratePlayStreamEvent": generate_play_stream_event,
			"RevisionSelection": revision_selection
		}
		return requests.post(
			f"{self.api}/Client/ExecuteCloudScript",
			json=data,
			headers=self.headers).json()
		
	def get_user_data(self, user_id: str) -> dict:
		data = {
			"PlayFabId": user_id
		}
		return requests.post(
			f"{self.api}/Client/GetUserData",
			json=data,
			headers=self.headers).json()
	
	def get_player_statistics(self) -> dict:
		return requests.post(
			f"{self.api}/Client/GetPlayerStatistics",
			headers=self.headers).json()
	
	def get_inventory(self) -> dict:
		return requests.post(
			f"{self.api}/Client/GetUserInventory",
			headers=self.headers).json()
	

	def get_catalog_items(self) -> dict:
		return requests.post(
			f"{self.api}/Client/GetCatalogItems",
			headers=self.headers).json()
