<template>
  <div>
    <v-dialog
      v-model="this.addExerciseScreen"
      persistent
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card tile>
        <v-toolbar dark color="deep-orange darken-4">
          <v-btn icon dark @click="this.closeAddExercise">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Add Exercise</v-toolbar-title>
          <div class="flex-grow-1"></div>
        </v-toolbar>
          <v-list-item-group>
            <template v-for="(item, index) in exercises">
              <v-list-item :key="item">
                <v-list-item-content>
                  <v-list-item-title>{{ item }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-divider :key="index"></v-divider>
            </template>
          </v-list-item-group>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'AddExercise',
  data() {
    return {
      exercises: ['memes', 'guy', 'dude'],
    };
  },
  computed: {
    ...mapState([
      'addExerciseScreen',
    ]),
  },
  components: {
  },
  methods: {
    ...mapActions([
      'closeAddExercise',
    ]),
  },
};
</script>
