class BomberFriends {
	constructor() {
		this.api = "https://e1e6.playfabapi.com"
		this.headers = {
			"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
			"x-playfabsdk": "Cocos2d-xSDK-0.40.180529",
			"content-type": "application/json",
			"connection": "keep_alive"
		}
		this.titleId = "E1E6"
	}

	async loginWithCustomId(customId, createAccount = true) {
		const response = await fetch(
			`${this.api}/Client/LoginwithCustomID`, {
				method: "POST",
				body: JSON.stringify({
					createAccount: createAccount,
					CustomId: customId,
					TitleId: this.titleId
				}),
				headers: this.headers
			})
		const data = await response.json()
		if ("SessionTicket" in data.data) {
			this.customId = customId
			this.userId = data.data.PlayFabID
			this.sessionTicket = data.data.SessionTicket
			this.entityToken = data.data.EntityToken.EntityToken
			this.headers["x-authorization"] = this.sessionTicket
			this.headers["x-entitytoken"] = this.entityToken
		}
		return data
	}

	
	async getEntityToken() {
		const response = await fetch(
			`${this.api}/Authentication/GetEntityToken`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async getTitleData(keys = ["ScriptVersionAndroid"]) {
		const response = await fetch(
			`${this.api}/Client/GetTitleData`, {
				method: "POST",
				body: JSON.stringify({
					keys: keys
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getServerStatus(platform = "android", generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "getServerStatus",
					FunctionParameter: {
						platform: platform
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async updateDisplayName(displayName) {
		const response = await fetch(
			`${this.api}/Client/UpdateUserTitleDisplayName`, {
				method: "POST",
				body: JSON.stringify({
					DisplayName: displayName
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getLeaderboard(
		maxResultsCount = 100,
			startPosition = 0,
			statisticName = "Trophies",
			showAvatarUrl = false,
			showBannedUntil = false,
			showCampaignAttributions = false,
			showContactEmailAddresses = false,
			showCreated = false,
			showDisplayName = true,
			showLastLogin = false,
			showLinkedAccounts = false,
			showLocations = false,
			showMemberships = false,
			showOrigination = false,
			showPushNotificationRegistrations = false,
			showStatistics = false,
			showTags = true,
			showTotalValueToDateInUsd = false,
			showValuesToDate = false) {
		const response = await fetch(
			`${this.api}/Client/GetLeaderboard`, {
				method: "POST",
				body: JSON.stringify({
					MaxResultsCount: maxResultsCount,
					ProfileConstraints: {
						ShowAvatarUrl: showAvatarUrl,
						ShowBannedUntil: showBannedUntil,
						ShowCampaignAttributions: showCampaignAttributions,
						ShowContactEmailAddresses: showContactEmailAddresses,
						ShowCreated: showCreated,
						ShowDisplayName: showDisplayName,
						ShowLastLogin: showLastLogin,
						ShowLinkedAccounts: showLinkedAccounts,
						ShowLocations: showLocations,
						ShowMemberships: showMemberships,
						ShowOrigination: showOrigination,
						ShowPushNotificationRegistrations: showPushNotificationRegistrations,
						ShowStatistics: showStatistics,
						ShowTags: showTags,
						ShowTotalValueToDateInUsd: showTotalValueToDateInUsd,
						ShowValuesToDate: showValuesToDate,
					},
					StartPosition: startPosition,
					StatisticName: statisticName}),
				headers: this.headers
			})
		return response.json()
	}

	async claimSeasonPrize(name, id = 0, isFree = true, generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "claimSeasonPrize",
					FunctionParameter: {
						id: id,
						isFree: isFree,
						name: name
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getInitialData(
			version = 756,
			platform = "android",
			pdDatas = ["deckslots", "dungeonrundata", "testidata"],
			rodDatas = ["_clandata"], 
			generatePlayStreamEvent = false,
			revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "getInitialData",
					FunctionParameter: {
						version: version,
						platform: platform,
						pddatas: pdDatas,
						poddatas: rodDatas
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async claimReward(id = 0, rewardSpin = false, name = "Wheel", generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "claimReward",
					FunctionParameter: {
						id: id,
						reward_spin: rewardSpin,
						name: name
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getSinglePlayerReward(level, type = 0, generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "getSinglePlayerReward",
					FunctionParameter: {
						level: level,
						type: type
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async saveUserData(data, generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "saveBomberUserData",
					FunctionParameter: {
						data: data
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async openSlot(slot, cost = 0, generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "tryStartOpeningSlotChest",
					FunctionParameter: {
						slot: slot,
						cost: cost
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async updateUserData(data, permission = "private") {
		const response = await fetch(
			`${this.api}/Client/UpdateUserData`, {
				method: "POST",
				body: JSON.stringify({
					Data: data,
					Permission: permission
				}),
				headers: this.headers
			})
		return response.json()
	}

	async tutorialWon(standing = 0, generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "tutorialWon",
					FunctionParameter: {
						standing: standing
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async addFashionPoints(points, ad = false, generatePlayStreamEvent = false, revisionSelection = "live") {
		const response = await fetch(
			`${this.api}/Client/ExecuteCloudScript`, {
				method: "POST",
				body: JSON.stringify({
					FunctionName: "addFashionPoints",
					FunctionParameter: {
						points: points,
						ad: ad
					},
					GeneratePlayStreamEvent: generatePlayStreamEvent,
					RevisionSelection: revisionSelection
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getUserData(userId) {
		const response = await fetch(
			`${this.api}/Client/GetUserData`, {
				method: "POST",
				body: JSON.stringify({
					PlayFabID: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getPlayerStatistics() {
		const response = await fetch(
			`${this.api}/Client/GetPlayerStatistic`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async getInventory() {
		const response = await fetch(
			`${this.api}/Client/GetUserInventory`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async getCatalogItems() {
		const response = await fetch(
			`${this.api}/Client/GetCatalogItems`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {BomberFriends}
