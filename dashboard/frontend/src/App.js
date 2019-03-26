import React from "react";
import Main from "./components/Main";
import Transcript from "./components/Transcript";
import { Grid, AppBar, Toolbar, Typography } from "@material-ui/core";

const App = () => (
  <div>
    <div
      style={{
        flexGrow: 1,
        backgroundColor: "#FCFCFC",
        color: "black",
        marginBottom: 20
      }}
    >
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" color="inherit">
            Mentalyst
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
    <Grid container direction="row">
      <Grid item xs={6}>
        <Main />
      </Grid>
      <Grid item xs={6}>
        <Transcript />
      </Grid>
    </Grid>
  </div>
);

export default App;
