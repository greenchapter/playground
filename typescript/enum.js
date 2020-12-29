var AccessLevels;
(function (AccessLevels) {
    AccessLevels[AccessLevels["User"] = 0] = "User";
    AccessLevels[AccessLevels["Admin"] = 1] = "Admin";
    AccessLevels[AccessLevels["Root"] = 2] = "Root";
})(AccessLevels || (AccessLevels = {}));
var user = {
    username: 'tott',
    accessLevel: AccessLevels.Root
};
