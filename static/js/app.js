
const close_alert = () => {
    let id = "alert_signup";
    let ele = document.getElementById(id);
    ele.remove();
}

const changeRole = (userID) => {
    confirm("Are you sure you want to change the role of "+userID+"?")
    ? document.getElementById("userForm_"+userID).submit()
    : null;
}