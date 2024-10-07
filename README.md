# bomber_friends.js
Mobile-API for [Bomber Friends](https://play.google.com/store/apps/details?id=com.hyperkani.bomberfriends) mobile game

## Example
```JavaScript
async function main() {
	const { BomberFriends } = require("./bomber_friends.js")
	const bomberFriends = new BomberFriends()
	await bomberFriends.loginWithCustomId("customOId")
}

main()
```
