<template>
  <div style="display: flex; justify-content: center">
    <table id="activites" class="activites">
      <thead>
        <tr>
          <th>ID</th>
          <th>Created On</th>
          <th>Updated On</th>
          <th>Completed</th>
          <th>Name</th>
          <th>Description</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(activity, index) in activities" :key="activity.id">
          <td>{{ activity.id }}</td>
          <td>{{ activity.created_on }}</td>
          <td>{{ activity.updated_on }}</td>
          <td>
            <input
              type="checkbox"
              :checked="activity.completed"
              @input="
                (ev) =>
                  $emit('changeStatus', {
                    value: ev.target.checked,
                    activityId: activity.id,
                    index,
                  })
              "
            />
          </td>
          <td>{{ activity.name }}</td>
          <td
            class="ellipsis"
            @mouseover="showTooltip = true"
            @mouseleave="showTooltip = false"
          >
            {{ activity.desc || "N/A" }}
            <div v-if="showTooltip" class="tooltip">
              {{ activity.desc || "N/A" }}
            </div>
          </td>
          <td>
            <button @click="$emit('delete', activity.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "HelloWorld",
  props: {
    activities: {
      type: Object,
      required: true,
    },
  },
  emits: ["delete", "changeStatus"],
  setup() {
    const showTooltip = ref(false);

    return {
      showTooltip,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
$breakpoint-alpha: 480px;

.ellipsis {
  max-width: 200px; /* Adjust the maximum width as needed */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  position: relative;
  cursor: pointer;
}

.tooltip {
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 5px;
  border-radius: 3px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 999;
  top: 100%;
  left: 0;
  display: none;
}

.ellipsis:hover + .tooltip {
  display: block;
}
.activites {
  background: #34495e;
  color: #fff;
  border-radius: 0.4em;
  overflow: hidden;
  tr {
    border-color: lighten(#34495e, 10%);
  }
  th,
  td {
    margin: 0.5em 1em;
    @media (min-width: $breakpoint-alpha) {
      padding: 1em !important;
    }
  }
  th,
  td:before {
    color: #dd5;
  }
}
</style>
