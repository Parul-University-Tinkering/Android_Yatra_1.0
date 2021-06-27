package com.example.nikhilportfolio;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ActivityOptions;
import android.content.Intent;
import android.os.Bundle;
import android.util.Pair;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView textView1,textView2;
    RelativeLayout r1,r2;
    ImageView img1,img2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        r1=findViewById(R.id.relativeLayout);
        r2=findViewById(R.id.relativeLayout2);

        textView1=findViewById(R.id.linetv1);
        textView2=findViewById(R.id.linetv11);


        img1=findViewById(R.id.img1);
        Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.right_to_left);
        img1.startAnimation(animation1);

        img2=findViewById(R.id.img2);
        Animation animation2 = AnimationUtils.loadAnimation(this, R.anim.right_to_left2);
        img2.startAnimation(animation2);

        r1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent =new Intent(MainActivity.this,Form.class);

                Pair[] pairs = new Pair[3];
                pairs[0] = new Pair<View, String>(r1,"abc");
                pairs[1] = new Pair<View, String>(textView1,"aaa");
                pairs[2] = new Pair<View, String>(img1,"xyz");

                ActivityOptions options = ActivityOptions.makeSceneTransitionAnimation(MainActivity.this,pairs);
                startActivity(intent, options.toBundle());
            }
        });


        r2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent =new Intent(MainActivity.this,Form2.class);

                Pair[] pairs = new Pair[3];
                pairs[0] = new Pair<View, String>(r2,"abc");
                pairs[1] = new Pair<View, String>(textView2,"aaa");
                pairs[2] = new Pair<View, String>(img2,"xyz");

                ActivityOptions options = ActivityOptions.makeSceneTransitionAnimation(MainActivity.this,pairs);
                startActivity(intent, options.toBundle());
            }
        });

    }
}