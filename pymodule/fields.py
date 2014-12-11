#data that can be accessed through Pyet

INT = ['inuse', 'spawnflags', 'neverFree', 'flags', 'freetime', 'eventTime', 'freeAfterEvent', 'unlinkAfterEvent', 'physicsObject', 'physicsBounce', 'clipmask', 'realNonSolidBModel', 'timestamp', 'angle', 'targetnamehash', 'speed', 'closespeed', 'gDuration', 'gDurationBack', 'nextthink', 'health', 'takedamage', 'damage', 'splashDamage', 'splashRadius', 'methodOfDeath', 'splashMethodOfDeath', 'count', 'watertype', 'waterlevel', 'noise_index', 'wait', 'random', 'radius', 'delay', 'TargetFlag', 'duration', 'dl_atten', 'key', 'harc', 'varc', 'props_frame_state', 'missionLevel', 'start_size', 'end_size', 'isProp', 'mg42BaseEnt', 'flameQuota', 'flameQuotaTime', 'flameBurnEnt', 'count2', 'grenadeExplodeTime', 'grenadeFired', 'numScriptEvents', 'accuracy', 'spawnTime', 'tagNumber', 'linkTagTime', 'backdelta', 'back', 'moving', 'surfaceFlags', 'mg42weapHeat', 'runthisframe', 'numPlayers', 'partofstage', 'deathType', 'r.bmodel', 'r.contents', 'r.eventTime', 'r.linkcount', 'r.linked', 'r.ownerNum', 'r.singleClient', 'r.svFlags', 'r.worldflags', 's.clientNum', 's.constantLight', 's.density', 's.dl_intensity', 's.dmgFlags', 's.eFlags', 's.eType', 's.effect1Time', 's.effect3Time', 's.frame', 's.groundEntityNum', 's.loopSound', 's.modelindex', 's.modelindex2', 's.number', 's.onFireEnd', 's.onFireStart', 's.powerups', 's.solid', 's.teamNum', 's.time', 's.time2', 's.weapon']

STRING = ['classname', 'model', 'model2', 'message', 'target', 'targetname', 'team', 'aiName', 'aiSkin', 'dl_stylestring', 'dl_shader', 'spawnitem', 'track', 'scriptName', 'constages', 'desstages', 'damageparent', 'tagName']


VEC3_T = ['rotate', 'TargetAngles', 'dl_color', 'oldOrigin', 's.origin', 's.origin2', 'r.absmax', 'r.absmin', 'r.currentAngles', 'r.currentOrigin', 'r.maxs', 'r.mins', 's.angles', 's.angles2']

#(ent->client->*)
CLIENT = ['sess.playerType', 'sess.playerWeapon', 'sess.playerWeapon2', 'sess.spawnObjectiveIndex', 'sess.latchPlayerType', 'sess.latchPlayerWeapon', 'sess.damage_given', 'sess.damage_received', 'sess.deaths', 'sess.game_points', 'sess.kills', 'sess.muted', 'sess.rank', 'sess.referee', 'sess.rounds', 'sess.spec_invite', 'sess.spec_team', 'sess.suicides', 'sess.team_damage', 'sess.team_kills', 'sess.spectatorClient', 'sess.spectatorState', 'pers.localClient', 'pers.initialSpawn', 'pers.enterTime', 'pers.connectTime', 'pers.teamState.state', 'pers.voteCount', 'pers.teamVoteCount', 'pers.complaints', 'pers.complaintClient', 'pers.complaintEndTime', 'pers.lastReinforceTime', 'pers.applicationClient', 'pers.applicationEndTime', 'pers.invitationClient', 'pers.invitationEndTime', 'pers.propositionClient', 'pers.propositionClient2', 'pers.propositionEndTime', 'pers.autofireteamEndTime', 'pers.autofireteamCreateEndTime', 'pers.autofireteamJoinEndTime', 'pers.lastSpawnTime', 'pers.ready', 'pers.connected', 'pers.teamState.state', 'ps.ping']

INTARRAY=["ps.stats", "ps.persistant", "ps.powerups","ps.ammo", "ps.ammoclip"]


Type = {"int" : INT, "string" : STRING, "vec3t" : VEC3_T, "client" : CLIENT }

