using System;
using UnityEngine;

public class Player : MonoBehaviour
{
    [SerializeField]
    private float speed = 10;

    private const float SCREEN_BOUND_X = 9;
    private const float SCREEN_BOUND_Y = 5;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        MovePlayer();
        CheckScreenBounds();
    }

    private void CheckScreenBounds()
    {
        if (transform.position.x > SCREEN_BOUND_X)
        {
            transform.position = new Vector3(-SCREEN_BOUND_X, transform.position.y);
        }

        if (transform.position.x < -SCREEN_BOUND_X)
        {
            transform.position = new Vector3(SCREEN_BOUND_X, transform.position.y);
        }

        if (transform.position.y > SCREEN_BOUND_Y)
        {
            transform.position = new Vector3(transform.position.x , -SCREEN_BOUND_Y);
        }

        if (transform.position.y < -SCREEN_BOUND_Y)
        {
            transform.position = new Vector3(transform.position.x, SCREEN_BOUND_Y);
        }
    }

    private void MovePlayer()
    {
        float inputHorizontal = Input.GetAxis("Horizontal");
        float inputVertical = Input.GetAxis("Vertical");

        Vector3 position = new(inputHorizontal, inputVertical);
        transform.Translate(speed * Time.deltaTime * position);
    }
}
