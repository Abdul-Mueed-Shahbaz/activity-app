<template>
  <div class="home">
    <h1>Activity List</h1>
    <div class="padding-bottom__30px">
      <button @click="() => toggleActivityForm()">Add Activity</button>
    </div>
    <activity-form
      v-if="addActivity"
      @close="() => toggleActivityForm()"
      @onFormSubmit="
        () => {
          initFetchActivityList();
          toggleActivityForm();
        }
      "
    />
    <activity-table
      :activities="activities"
      @delete="(activityId) => initDeleteActivity(activityId)"
      @changeStatus="(ev) => initChangeActivityStatus(ev)"
    />
  </div>
</template>

<script>
import { useStore } from "vuex";
import { defineComponent, onMounted, ref } from "vue";

import ActivityTable from "@/components/ActivityTable.vue";
import ActivityForm from "@/components/ActivityForm.vue";

export default defineComponent({
  name: "home-view",
  components: {
    ActivityTable,
    ActivityForm,
  },
  props: {
    msg: String,
  },
  setup() {
    const store = useStore();
    const activities = ref([]);
    const addActivity = ref(false);

    function toggleActivityForm() {
      addActivity.value = !addActivity.value;
    }
    function initDeleteActivity(activityId) {
      store.dispatch("activity/deleteActivity", activityId).then(() => {
        initFetchActivityList();
      });
    }

    function initFetchActivityList() {
      store.dispatch("activity/fetchActivityList").then((response) => {
        activities.value = response;
      });
    }
    function initChangeActivityStatus({ value, activityId, index }) {
      store
        .dispatch("activity/updateActivityStatus", {
          activityId,
          completed: value,
        })
        .catch(() => {
          activities.value[index].completed = !value;
        });
    }
    onMounted(() => {
      initFetchActivityList();
    });
    return {
      addActivity,
      activities,
      toggleActivityForm,
      initDeleteActivity,
      initChangeActivityStatus,
      initFetchActivityList,
    };
  },
});
</script>

<style>
.padding-bottom__30px {
  padding-bottom: 30px;
  padding-top: 5px;
}
</style>
