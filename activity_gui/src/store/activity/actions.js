import { baseUrl } from "@/common/constants/config";

const baseEndpoint = baseUrl + "activity/";

export async function deleteActivity(_, activityId) {
  try {
    const response = await fetch(`${baseEndpoint}${activityId}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    return err;
  }
}

export async function updateActivityStatus(_, { activityId, completed }) {
  if (!activityId) {
    throw new Error("Invalid payload");
  }
  try {
    const response = await fetch(`${baseEndpoint}${activityId}/`, {
      method: "PATCH",
      body: JSON.stringify({
        completed,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    return err;
  }
}

export async function fetchActivityList() {
  try {
    const response = await fetch(baseEndpoint);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    return err;
  }
}

export async function createActivty(_, payload) {
  try {
    const response = await fetch(baseEndpoint, {
      method: "POST",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    return err;
  }
}

export function updateFormName({ commit }, name) {
  commit("setFormName", name);
}
export function updateFormDescription({ commit }, description) {
  commit("setFormDescription", description);
}
