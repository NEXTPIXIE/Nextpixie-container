export const isAuthenticated = () => {
  if (localStorage.getItem("token")) {
    return true;
  } else {
    return false;
  }
};

export const isActive = (history, path) => {
  let activeScreen = history.pathname === path ? true : false;
  return activeScreen;
};
